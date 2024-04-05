## Order Management System - RESTful APIs (**link to your GitHub repository here**)

This project implements a set of RESTful APIs for order management, designed to orchestrate communication between various enterprise systems. The APIs are intended to be used by a customer-facing website for functionalities like:
* **Signup as a new user**
* **Login**
* **Get product price quotes**
* **Add product to Product DB**
* **Submit purchase orders**

**Architecture Diagram:**

![Alt text](https://github.com/suryakamalog/order-management/blob/main/order-management-architecture.png "Architecture diagram")

**Key Features:**

* **RESTful API Design:** Enables seamless integration with the customer-facing website.
* **Scalability Considerations:** Designed for horizontal scaling to handle increasing load. (Mention specific approaches used if applicable, e.g., stateless design, caching)

**Getting Started:**

1. **Clone the repository:**  
   ```bash
   git clone https://github.com/suryakamalog/order-management.git
   ```
2. **Prerequisites:**
   * Start all services
   ```bash
   docker-compose -f docker-compose.yml up
   ```
   * Stop all services
   ```bash
   docker-compose -f docker-compose.yml down
   ```
4. **Setup:**
   * Run 
6. **API Documentation:** Access swagger using [127.0.0.1/](http://127.0.0.1:5001/)

