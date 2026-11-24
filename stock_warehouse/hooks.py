# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "stock_warehouse"
app_title = "Erpnext Stock Inventory Warehouse Engine"
app_publisher = "Shyamkumar Pandey"
app_description = "Erpnext Stock Inventory Warehouse Engine - Enterprise Multi-DocType Solution for Frappe & ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/stock_warehouse/css/stock_warehouse.bundle.css"
app_include_js = "/assets/stock_warehouse/js/stock_warehouse.bundle.js"

# Document Events
# ---------------
doc_events = {
    "Erpnext Stock Inventory Warehouse Engine Entry": {
        "validate": "stock_warehouse.services.validator.EnterpriseValidationEngine.validate_compliance_rules",
        "on_submit": "stock_warehouse.services.integration_service.EnterpriseIntegrationService.verify_remote_status"
    }
}

# Scheduled Background Tasks
# --------------------------
scheduler_events = {
    "hourly": [
        "stock_warehouse.tasks.hourly_sync"
    ],
    "daily": [
        "stock_warehouse.tasks.daily_reconciliation"
    ],
    "weekly": [
        "stock_warehouse.tasks.weekly_digest"
    ]
}
