# 📋 Customer Management REST API

A clean, beginner-friendly REST API built with **FastAPI** and **Python** for managing customer data. Supports full CRUD operations, Pydantic validation, and comes pre-loaded with 10 sample customers.

---

## 🚀 Quick Start

### 1. Install dependencies

```bash
pip install fastapi uvicorn pydantic[email]
```

### 2. Run the server

```bash
uvicorn main:app --reload
```

### 3. Open the interactive docs

```
http://127.0.0.1:8000/docs
```

> The `--reload` flag auto-restarts the server whenever you save changes to `main.py`.

---

## 📁 Project Structure

```
customer-api/
│
└── main.py          # All application code (models, routes, storage)
└── README.md        # Project documentation
```

---

## 🗄️ Data Model

Each customer record contains the following fields:

| Field   | Type   | Validation                  |
|---------|--------|-----------------------------|
| `id`    | int    | Auto-assigned, read-only    |
| `name`  | string | Minimum 3 characters        |
| `email` | string | Must be a valid email format|
| `age`   | int    | Must be between 18 and 100  |

### Sample Customer Record

```json
{
  "id": 1,
  "name": "Alice Johnson",
  "email": "alice.johnson@example.com",
  "age": 28
}
```

---

## 🌐 API Endpoints

| Method   | Endpoint              | Description              | Status Code |
|----------|-----------------------|--------------------------|-------------|
| `GET`    | `/customers`          | Retrieve all customers   | 200         |
| `GET`    | `/customers/{id}`     | Retrieve a single customer | 200 / 404 |
| `POST`   | `/customers`          | Create a new customer    | 201         |
| `PUT`    | `/customers/{id}`     | Update an existing customer | 200 / 404 |
| `DELETE` | `/customers/{id}`     | Delete a customer        | 200 / 404  |

---

## 📖 Usage Examples

### Get all customers
```bash
curl -X GET http://127.0.0.1:8000/customers
```

### Get a single customer
```bash
curl -X GET http://127.0.0.1:8000/customers/1
```

### Create a new customer
```bash
curl -X POST http://127.0.0.1:8000/customers \
  -H "Content-Type: application/json" \
  -d '{"name": "Jane Doe", "email": "jane.doe@example.com", "age": 30}'
```

### Update a customer (partial update supported)
```bash
curl -X PUT http://127.0.0.1:8000/customers/1 \
  -H "Content-Type: application/json" \
  -d '{"age": 29}'
```

### Delete a customer
```bash
curl -X DELETE http://127.0.0.1:8000/customers/1
```

---

## ✅ Validation Rules

Requests are validated automatically using **Pydantic**. If a rule is violated, the API returns a `422 Unprocessable Entity` response with a detailed error message.

| Field   | Rule                                         |
|---------|----------------------------------------------|
| `name`  | Must be at least **3 characters** long       |
| `email` | Must follow a **valid email format**         |
| `age`   | Must be an integer **between 18 and 100**    |

### Example validation error response

```json
{
  "detail": [
    {
      "loc": ["body", "age"],
      "msg": "ensure this value is greater than or equal to 18",
      "type": "value_error.number.not_ge"
    }
  ]
}
```

---

## 🌱 Pre-seeded Sample Data

The API starts with 10 customers already loaded in memory:

| ID | Name            | Email                          | Age |
|----|-----------------|--------------------------------|-----|
| 1  | Alice Johnson   | alice.johnson@example.com      | 28  |
| 2  | Bob Smith       | bob.smith@example.com          | 35  |
| 3  | Carol Williams  | carol.williams@example.com     | 42  |
| 4  | David Brown     | david.brown@example.com        | 23  |
| 5  | Eva Martinez    | eva.martinez@example.com       | 31  |
| 6  | Frank Lee       | frank.lee@example.com          | 55  |
| 7  | Grace Kim       | grace.kim@example.com          | 19  |
| 8  | Henry Davis     | henry.davis@example.com        | 47  |
| 9  | Isla Thompson   | isla.thompson@example.com      | 26  |
| 10 | Jack Wilson     | jack.wilson@example.com        | 38  |

> ⚠️ **Note:** Storage is in-memory only. All data resets when the server restarts.

---

## 🧩 Pydantic Models

The project uses three separate models to keep input and output clean:

| Model              | Purpose                                      |
|--------------------|----------------------------------------------|
| `CustomerCreate`   | Validates the body of `POST` requests        |
| `CustomerUpdate`   | Validates `PUT` requests (all fields optional)|
| `CustomerResponse` | Shapes the data returned to the client       |

---

## 🛠️ Tech Stack

| Tool       | Purpose                             |
|------------|-------------------------------------|
| Python 3.10+ | Programming language              |
| FastAPI    | Web framework for building the API  |
| Pydantic   | Data validation and serialisation   |
| Uvicorn    | ASGI server to run the application  |

---

## 📚 Interactive API Documentation

FastAPI automatically generates two documentation UIs:

| UI         | URL                                    |
|------------|----------------------------------------|
| Swagger UI | http://127.0.0.1:8000/docs             |
| ReDoc      | http://127.0.0.1:8000/redoc            |

Use the Swagger UI to test all endpoints directly from your browser — no extra tools needed.

---

## 🔮 Future Improvements

- [ ] Connect to a real database (e.g., PostgreSQL with SQLAlchemy)
- [ ] Add authentication (e.g., JWT tokens)
- [ ] Add pagination for `GET /customers`
- [ ] Write automated tests with `pytest`
- [ ] Dockerise the application

---

## 📄 License

This project is open source and free to use for learning purposes.
