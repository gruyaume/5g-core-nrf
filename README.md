
# 5G Core Network Repository Function

> :warning: This project is under construction!


The Network Function (NF) Repository Function (NRF) is the network entity in the 5G Core Network (5GC)
supporting the following functionality:
- Maintains the NF profile of available NF instances and their supported services;
- Allows other NF instances to subscribe to, and get notified about, the registration in NRF of new NF instances of
a given type;
- Supports service discovery function. It receives NF Discovery Requests from NF instances, and provides the
information of the available NF instances fulfilling certain criteria (e.g., supporting a given service)

## Usage
Run the server using uvicorn:
```bash
cd src
uvicorn main:app --reload
```

### Database
This service relies on a relationship with a PostgreSQL database. Database connectivity information
is passed through environment variables.

## Reference

### Framework
This project leverages [FastAPI](https://github.com/tiangolo/full-stack-fastapi-postgresql) web
  framework. 

### 5G Specification
This service has been created following the 
[ETSI specification for the NRF](https://www.etsi.org/deliver/etsi_ts/129500_129599/129510/15.03.00_60/ts_129510v150300p.pdf).
Some common data models are also taken from this [specification sheet](https://www.etsi.org/deliver/etsi_ts/129500_129599/129571/15.03.00_60/ts_129571v150300p.pdf) from ETSI.
