#!/usr/bin/env python3
"""
數據遷移腳本：將現有的FoodItem商品同步到超商庫存系統
根據商品分類自動分配架位和儲存條件
"""

import sys
import os
from datetime import datetime

# 將專案根目錄添加到 sys.path
project_root = os.path.abspath(os.path.dirname(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.main import app, db
from src.models.food_item import FoodItem

# 分類到架位的映射
CATEGORY_TO_LOCATION = {
    '乳製品': ('A1', '冷藏'),
    '肉類': ('A2', '冷藏'),
    '海鮮': ('A3', '冷藏'),
    '蔬菜': ('B1', '常溫'),
    '水果': ('B2', '常溫'),
    '飲料': ('B3', '常溫'),
    '零食': ('C1', '常溫'),
    '烘焙': ('C2', '常溫'),
    '調味料': ('C3', '常溫'),
    '冷凍食品': ('D1', '冷凍'),
    '其他': ('E1', '常溫'),
}

def migrate_data():
    """執行數據遷移"""
    with app.app_context():
        print("=" * 60)
        print("開始數據遷移：同步現有商品到超商庫存系統")
        print("=" * 60)
        
        # 查詢所有現有的FoodItem
        all_items = FoodItem.query.all()
        print(f"\n找到 {len(all_items)} 件現有商品")
        
        if len(all_items) == 0:
            print("沒有現有商品需要遷移")
            return
        
        # 統計變量
        updated_count = 0
        error_count = 0
        
        # 遍歷所有商品
        for item in all_items:
            try:
                # 根據分類分配架位和儲存條件
                category = item.category or '其他'
                
                if category in CATEGORY_TO_LOCATION:
                    location, condition = CATEGORY_TO_LOCATION[category]
                else:
                    location, condition = CATEGORY_TO_LOCATION['其他']
                
                # 更新商品信息
                item.storage_location = location
                item.storage_condition = condition
                item.item_status = '在庫'
                item.ai_check_status = 'Pass'
                item.inbound_date = item.created_at or datetime.now()
                
                # 如果沒有設置單位價格，保持默認值0.0
                if item.unit_price is None:
                    item.unit_price = 0.0
                
                print(f"✓ 更新商品 ID={item.id}, 名稱='{item.name}', 架位={location}, 儲存條件={condition}")
                updated_count += 1
                
            except Exception as e:
                print(f"✗ 更新商品 ID={item.id} 失敗: {str(e)}")
                error_count += 1
        
        # 提交更改
        try:
            db.session.commit()
            print(f"\n" + "=" * 60)
            print(f"數據遷移完成！")
            print(f"成功更新: {updated_count} 件商品")
            print(f"失敗: {error_count} 件商品")
            print("=" * 60)
        except Exception as e:
            db.session.rollback()
            print(f"\n提交更改失敗: {str(e)}")
            print("所有更改已回滾")

if __name__ == '__main__':
    migrate_data()
