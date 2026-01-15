# AirBnB Clone — Command Interpreter

## 📌 Project Description

This project is the first step toward building a full web application: an **AirBnB clone**.  
In this phase, we implement a **command-line command interpreter (console)** to manage application objects and handle their persistence using JSON serialization.

The console allows us to:
- Create new objects (User, BaseModel, etc.)
- Retrieve stored objects
- Update object attributes
- Delete objects
- Persist objects to a JSON file

Later stages of the project will reuse this foundation for:
- HTML/CSS templating
- Database storage
- RESTful API
- Front-end integration

---

## 🧠 Learning Objectives

By completing this project, we learn how to:

- Create Python packages
- Build a command interpreter using the `cmd` module
- Use `*args` and `**kwargs`
- Serialize and deserialize objects
- Work with JSON files
- Manage dates using `datetime`
- Generate unique IDs using `uuid`
- Write and run unit tests using `unittest`

---

## ⚙️ Technologies Used

- Python 3.8.5
- Ubuntu 20.04 LTS
- JSON for data persistence
- `cmd`, `uuid`, `datetime`, `unittest` modules

---


---

## 🖥️ Command Interpreter Description

The command interpreter is similar to a shell but specialized to manage AirBnB objects.

It supports:

- Creating objects
- Showing objects
- Destroying objects
- Listing all objects
- Updating object attributes

---

## ▶️ How to Start the Console

### Interactive Mode

```bash
$ ./console.py
(hbnb)


