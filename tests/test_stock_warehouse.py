import unittest
from stock_warehouse.engine import ERPNextStockWarehouseEngine, FIFOBatch, WarehouseBalance

class TestStockWarehouse(unittest.TestCase):
    def test_fifo_consumption(self):
        engine = ERPNextStockWarehouseEngine()
        batches = [
            FIFOBatch("B1", 10.0, 100.0), # 10 @ ₹100 = 1000
            FIFOBatch("B2", 20.0, 120.0)  # 20 @ ₹120
        ]
        # Consume 15 items -> 10 from B1 (₹1000) + 5 from B2 (₹600) = ₹1600
        cogs = engine.consume_stock_fifo(batches, 15.0)
        self.assertEqual(cogs, 1600.0)
        self.assertEqual(batches[0].qty_remaining, 0.0)
        self.assertEqual(batches[1].qty_remaining, 15.0)

    def test_reorder_level_alert(self):
        engine = ERPNextStockWarehouseEngine()
        bal = WarehouseBalance("Main Warehouse", "SKU-BEARING", 12.0, reorder_level=20.0, reorder_qty=50.0)
        qty = engine.check_reorder_trigger(bal)
        self.assertEqual(qty, 50.0)

if __name__ == "__main__":
    unittest.main()
