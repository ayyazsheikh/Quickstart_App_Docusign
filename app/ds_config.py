# ds_config.py
#
# DocuSign configuration settings

DS_CONFIG = {
    "ds_client_id": "5e65a104-a6f4-494d-9c9b-c55e8156aff3",  # The app's DocuSign integration key
    "ds_client_secret": "97fb1e87-5d2a-4d9b-bcca-c92735009437",  # The app's DocuSign integration key's secret
    "organization_id": "{ORGANIZATION_ID}", # A GUID value that identifies the organization
    "signer_email": "ayyaz.sheikh@educative.io",
    "signer_name": "Ayyaz Sheikh",
    "app_url": "http://localhost:5000",  # The URL of the application. Eg http://localhost:5000
    # NOTE: You must add a Redirect URI of appUrl/ds/callback to your Integration Key.
    #       Example: http://localhost:5000/ds/callback
    "authorization_server": "https://account-d.docusign.com",
    "click_api_client_host": "https://demo.docusign.net/clickapi",
    "rooms_api_client_host": "https://demo.rooms.docusign.com/restapi",
    "monitor_api_client_host": "https://lens-d.docusign.net",
    "admin_api_client_host": "https://api-d.docusign.net/management",
    "allow_silent_authentication": True,  # a user can be silently authenticated if they have an
    # active login session on another tab of the same browser
    "target_account_id": None,  # Set if you want a specific DocuSign AccountId,
    # If None, the user's default account will be used.
    "demo_doc_path": "demo_documents",
    "doc_salary_docx": "World_Wide_Corp_salary.docx",
    "doc_docx": "World_Wide_Corp_Battle_Plan_Trafalgar.docx",
    "doc_pdf": "World_Wide_Corp_lorem.pdf",
    "doc_terms_pdf": "Term_Of_Service.pdf",
    "doc_txt": "Welcome.txt",
    # Payment gateway information is optional
    "gateway_account_id": "{DS_PAYMENT_GATEWAY_ID}",
    "gateway_name": "stripe",
    "gateway_display_name": "Stripe",
    "github_example_url": "https://github.com/docusign/code-examples-python/tree/master/app/eSignature/examples/",
    "monitor_github_url": "https://github.com/docusign/code-examples-python/tree/master/app/monitor/examples/",
    "admin_github_url": "https://github.com/docusign/code-examples-python/tree/master/app/admin/examples/",
    "click_github_url": "https://github.com/docusign/code-examples-python/tree/master/app/click/examples/",
    "documentation": "",  # Use an empty string to indicate no documentation path.
    "quickstart": "true"
}

DS_JWT = {
    "ds_client_id": "5e65a104-a6f4-494d-9c9b-c55e8156aff3",
    "ds_impersonated_user_id": "ece7dcaa-0df1-4116-90f0-fb5d1c7c108e",  # The id of the user.
    "private_key_file": "./app/private.key", # Create a new file in your repo source folder named private.key then copy and paste your RSA private key there and save it.
    "authorization_server": "account-d.docusign.com"
}
