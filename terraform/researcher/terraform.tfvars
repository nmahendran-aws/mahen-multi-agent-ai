# Part 4: Researcher Agent Configuration
# Copy this file to terraform.tfvars and update with your values

# Your AWS region for App Runner (can be any region with App Runner support)
aws_region = "us-east-1"

# Your OpenAI API key (get from https://platform.openai.com/api-keys)
openai_api_key = "sk-..."

# API endpoint from Part 3 (get from Terraform output or API Gateway console)
alex_api_endpoint = "https://01rg2bosjg.execute-api.us-east-1.amazonaws.com/prod/ingest"

# API key from Part 3 (get from API Gateway console)
alex_api_key = "wzLEehc4t98F6rcNYFRLG79vHcsv5Jd05JDAZ1L1"

# Enable automated research scheduler (optional, default is false)
scheduler_enabled = false
