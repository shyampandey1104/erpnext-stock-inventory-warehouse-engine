# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "stock_warehouse"
app_title = "Erpnext Stock Inventory Warehouse Engine"
app_publisher = "Shyamkumar Pandey"
app_description = "Erpnext Stock Inventory Warehouse Engine for Frappe and ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/stock_warehouse/css/stock_warehouse.bundle.css"
app_include_js = "/assets/stock_warehouse/js/stock_warehouse.bundle.js"

# Document Events
# ---------------
doc_events = {
    "DocType Event": {
        "on_submit": "stock_warehouse.engine.on_document_submit",
        "on_cancel": "stock_warehouse.engine.on_document_cancel"
    }
}

# Scheduled Tasks
# ---------------
scheduler_events = {
    "daily": [
        "stock_warehouse.engine.daily_scheduled_sync"
    ]
}
