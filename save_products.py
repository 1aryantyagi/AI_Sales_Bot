import json

PRODUCT_CATALOG = [
    {
        "id": "prod_001",
        "name": "Enterprise Cloud Suite",
        "description": "Comprehensive cloud solution with storage, compute, and analytics. Designed for businesses needing scalable infrastructure. Provides seamless integration with existing applications. Ensures high security and data redundancy. Optimized for high performance and uptime.",
        "price": 2999.99,
        "stripe_price_id": "price_1ABCDEF"
    },
    {
        "id": "prod_002",
        "name": "Business Intelligence Pro",
        "description": "Advanced analytics and reporting platform. Enables data-driven decision-making with real-time insights. Provides AI-powered predictive analytics. Supports multiple data sources and visualization tools. Ensures secure data governance and compliance.",
        "price": 1999.99,
        "stripe_price_id": "price_2GHIJKL"
    },
    {
        "id": "prod_003",
        "name": "AI Chatbot Assistant",
        "description": "An intelligent chatbot for automating customer service and support. Uses NLP to understand and respond naturally. Supports multi-channel integration, including websites and social media. Learns from interactions for improved responses. Ensures secure and reliable conversations.",
        "price": 899.99,
        "stripe_price_id": "price_3MNOPQR"
    },
    {
        "id": "prod_004",
        "name": "Cybersecurity Shield",
        "description": "Advanced security suite for protecting digital assets. Provides real-time threat detection and prevention. Includes firewall, intrusion detection, and malware scanning. Ensures compliance with industry security standards. Easy integration with enterprise IT infrastructure.",
        "price": 2499.99,
        "stripe_price_id": "price_4STUVWX"
    },
    {
        "id": "prod_005",
        "name": "DevOps Automation Suite",
        "description": "A complete CI/CD and DevOps automation toolkit. Enables seamless deployment and continuous integration. Supports multiple cloud platforms and containerization. Provides monitoring, logging, and performance optimization. Ensures collaboration between development and operations teams.",
        "price": 1799.99,
        "stripe_price_id": "price_5YZABCD"
    },
    {
        "id": "prod_006",
        "name": "Cloud Backup & Recovery",
        "description": "Automated cloud-based backup and disaster recovery solution. Ensures business continuity with instant data restoration. Provides encryption and secure storage. Supports multiple platforms and databases. Offers customizable backup schedules and alerts.",
        "price": 1299.99,
        "stripe_price_id": "price_6EFGHIJ"
    },
    {
        "id": "prod_007",
        "name": "AI-Powered CRM",
        "description": "A customer relationship management tool with AI-powered insights. Automates lead tracking, follow-ups, and customer interactions. Provides predictive analytics for sales forecasting. Integrates with email, social media, and messaging apps. Enhances customer experience with smart recommendations.",
        "price": 1599.99,
        "stripe_price_id": "price_7KLMNOP"
    },
    {
        "id": "prod_008",
        "name": "E-Commerce Accelerator",
        "description": "A complete e-commerce solution for businesses of all sizes. Supports multi-channel sales and payment gateways. Provides AI-driven product recommendations. Ensures fast, secure transactions with fraud detection. Includes analytics for customer insights and sales trends.",
        "price": 2199.99,
        "stripe_price_id": "price_8QRSTUV"
    },
    {
        "id": "prod_009",
        "name": "Remote Work Collaboration Suite",
        "description": "An all-in-one solution for remote team collaboration. Includes video conferencing, chat, and task management. Provides secure cloud storage and document sharing. Supports real-time editing and team productivity tracking. Ensures seamless integration with existing enterprise tools.",
        "price": 999.99,
        "stripe_price_id": "price_9WXYZAB"
    },
    {
        "id": "prod_010",
        "name": "AI Code Review Tool",
        "description": "Automates code reviews with AI-driven analysis. Detects security vulnerabilities and code inefficiencies. Provides real-time suggestions for optimization. Supports multiple programming languages and frameworks. Helps maintain high-quality coding standards.",
        "price": 1899.99,
        "stripe_price_id": "price_10CDEFGH"
    },
    {
        "id": "prod_011",
        "name": "AI-Powered Marketing Suite",
        "description": "An intelligent marketing automation tool. Personalizes campaigns based on user behavior. Uses AI to optimize ad targeting and budget allocation. Integrates with social media, email, and CRM systems. Provides advanced analytics for performance tracking.",
        "price": 2099.99,
        "stripe_price_id": "price_11IJKLMN"
    },
    {
        "id": "prod_012",
        "name": "HR & Payroll Management System",
        "description": "A cloud-based HR and payroll management solution. Automates salary processing, tax calculations, and compliance. Provides employee self-service portals. Supports attendance tracking and performance evaluations. Ensures data security and regulatory compliance.",
        "price": 1399.99,
        "stripe_price_id": "price_12OPQRST"
    },
    {
        "id": "prod_013",
        "name": "IoT Device Management Platform",
        "description": "Manages and monitors IoT devices at scale. Provides real-time insights and analytics. Ensures secure connectivity and firmware updates. Supports multiple IoT protocols and cloud integrations. Helps optimize device performance and efficiency.",
        "price": 2599.99,
        "stripe_price_id": "price_13UVWXYZ"
    },
    {
        "id": "prod_014",
        "name": "Blockchain Security Suite",
        "description": "A robust blockchain-based security platform. Ensures data integrity and secure transactions. Provides decentralized identity verification. Supports multi-chain interoperability. Helps businesses implement blockchain-based security solutions.",
        "price": 2899.99,
        "stripe_price_id": "price_14ABCDEFG"
    },
    {
        "id": "prod_015",
        "name": "AI-Powered Virtual Assistant",
        "description": "A smart AI assistant for managing tasks and schedules. Integrates with calendars, emails, and messaging apps. Provides voice and text-based interactions. Uses AI for contextual understanding and automation. Enhances productivity with proactive reminders and suggestions.",
        "price": 799.99,
        "stripe_price_id": "price_15HIJKLMN"
    },
    {
        "id": "prod_016",
        "name": "Predictive Maintenance Platform",
        "description": "AI-powered predictive maintenance for industrial equipment. Monitors real-time data to detect potential failures. Uses machine learning to optimize maintenance schedules. Reduces downtime and increases operational efficiency. Supports integration with IoT sensors and analytics dashboards.",
        "price": 2799.99,
        "stripe_price_id": "price_16OPQRSTU"
    },
    {
        "id": "prod_017",
        "name": "Supply Chain Optimization Suite",
        "description": "A data-driven platform for supply chain management. Uses AI to optimize inventory and logistics. Provides real-time tracking and demand forecasting. Integrates with ERP and procurement systems. Enhances efficiency and reduces operational costs.",
        "price": 2699.99,
        "stripe_price_id": "price_17VWXYZAB"
    },
    {
        "id": "prod_018",
        "name": "Cloud-Based ERP System",
        "description": "A scalable enterprise resource planning (ERP) solution. Unifies business operations across departments. Provides real-time financial, HR, and inventory management. Ensures compliance with global regulations. Supports integrations with existing enterprise applications.",
        "price": 3199.99,
        "stripe_price_id": "price_18CDEFGHI"
    },
    {
        "id": "prod_019",
        "name": "Data Privacy Compliance Suite",
        "description": "Ensures compliance with global data privacy regulations. Automates data protection and reporting processes. Provides real-time monitoring and risk assessment. Helps businesses manage user consent and data access. Supports GDPR, CCPA, and other compliance frameworks.",
        "price": 2399.99,
        "stripe_price_id": "price_19JKLMNOP"
    },
    {
        "id": "prod_020",
        "name": "Automated Document Processing",
        "description": "AI-driven document management and processing system. Extracts key data from scanned documents. Automates workflow approvals and compliance checks. Supports multiple file formats and integrations. Reduces manual processing time and errors.",
        "price": 1899.99,
        "stripe_price_id": "price_20QRSTUVWX"
    }
]

# Save the list as a JSON file
with open("product_catalog.json", "w") as file:
    json.dump(PRODUCT_CATALOG, file, indent=4)

print("Product catalog saved successfully!")
