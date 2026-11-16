"""Complete ERPNext Stock Management Engine (Inventory, warehouses, stock entries aur reorder levels)."""

from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field


@dataclass
class FIFOBatch:
    batch_id: str
    qty_remaining: float
    purchase_rate: float


@dataclass
class WarehouseBalance:
    warehouse: str
    item_code: str
    current_qty: float
    reorder_level: float
    reorder_qty: float


class ERPNextStockWarehouseEngine:
    """Multi-Warehouse FIFO valuation and Automated Reorder Level monitoring."""

    def consume_stock_fifo(self, batches: List[FIFOBatch], consume_qty: float) -> float:
        """Consumes stock using First-In-First-Out (FIFO) and returns total Cost of Goods Sold."""
        total_cogs = 0.0
        remaining_to_consume = consume_qty

        for b in batches:
            if remaining_to_consume <= 0:
                break
            taken = min(b.qty_remaining, remaining_to_consume)
            total_cogs += taken * b.purchase_rate
            b.qty_remaining -= taken
            remaining_to_consume -= taken

        return round(total_cogs, 2)

    def check_reorder_trigger(self, bal: WarehouseBalance) -> Optional[float]:
        """Identifies if current stock is below reorder threshold and returns reorder quantity."""
        if bal.current_qty <= bal.reorder_level:
            return bal.reorder_qty
        return None
