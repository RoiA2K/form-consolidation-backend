# Form Consolidation

Make filling up forms easier.

## Version: 1.0.0

### /api/forms/

#### GET

##### Responses

| Code | Description |
| ---- | ----------- |
| 200  |             |

##### Security

| Security Schema | Scopes |
| --------------- | ------ |
| cookieAuth      |        |
| basicAuth       |        |

#### POST

##### Responses

| Code | Description |
| ---- | ----------- |
| 201  |             |

##### Security

| Security Schema | Scopes |
| --------------- | ------ |
| cookieAuth      |        |
| basicAuth       |        |

### /api/forms/{id}/

#### GET

##### Parameters

| Name | Located in | Description                                   | Required | Schema  |
| ---- | ---------- | --------------------------------------------- | -------- | ------- |
| id   | path       | A unique integer value identifying this form. | Yes      | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200  |             |

##### Security

| Security Schema | Scopes |
| --------------- | ------ |
| cookieAuth      |        |
| basicAuth       |        |

#### PUT

##### Parameters

| Name | Located in | Description                                   | Required | Schema  |
| ---- | ---------- | --------------------------------------------- | -------- | ------- |
| id   | path       | A unique integer value identifying this form. | Yes      | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200  |             |

##### Security

| Security Schema | Scopes |
| --------------- | ------ |
| cookieAuth      |        |
| basicAuth       |        |

#### PATCH

##### Parameters

| Name | Located in | Description                                   | Required | Schema  |
| ---- | ---------- | --------------------------------------------- | -------- | ------- |
| id   | path       | A unique integer value identifying this form. | Yes      | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200  |             |

##### Security

| Security Schema | Scopes |
| --------------- | ------ |
| cookieAuth      |        |
| basicAuth       |        |

#### DELETE

##### Parameters

| Name | Located in | Description                                   | Required | Schema  |
| ---- | ---------- | --------------------------------------------- | -------- | ------- |
| id   | path       | A unique integer value identifying this form. | Yes      | integer |

##### Responses

| Code | Description      |
| ---- | ---------------- |
| 204  | No response body |

##### Security

| Security Schema | Scopes |
| --------------- | ------ |
| cookieAuth      |        |
| basicAuth       |        |

### /api/register/

#### POST

##### Responses

| Code | Description      |
| ---- | ---------------- |
| 200  | No response body |

##### Security

| Security Schema | Scopes |
| --------------- | ------ |
| cookieAuth      |        |
| basicAuth       |        |

### /api/schema/

#### GET

##### Description:

OpenApi3 schema for this API. Format can be selected via content negotiation.

- YAML: application/vnd.oai.openapi
- JSON: application/vnd.oai.openapi+json

##### Parameters

| Name   | Located in | Description | Required | Schema |
| ------ | ---------- | ----------- | -------- | ------ |
| format | query      |             | No       | string |
| lang   | query      |             | No       | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200  |             |

##### Security

| Security Schema | Scopes |
| --------------- | ------ |
| cookieAuth      |        |
| basicAuth       |        |

### /api/users/

#### GET

##### Responses

| Code | Description |
| ---- | ----------- |
| 200  |             |

##### Security

| Security Schema | Scopes |
| --------------- | ------ |
| cookieAuth      |        |
| basicAuth       |        |

#### POST

##### Responses

| Code | Description |
| ---- | ----------- |
| 201  |             |

##### Security

| Security Schema | Scopes |
| --------------- | ------ |
| cookieAuth      |        |
| basicAuth       |        |

### /api/users/{id}/

#### GET

##### Parameters

| Name | Located in | Description                                   | Required | Schema  |
| ---- | ---------- | --------------------------------------------- | -------- | ------- |
| id   | path       | A unique integer value identifying this user. | Yes      | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200  |             |

##### Security

| Security Schema | Scopes |
| --------------- | ------ |
| cookieAuth      |        |
| basicAuth       |        |

#### PUT

##### Parameters

| Name | Located in | Description                                   | Required | Schema  |
| ---- | ---------- | --------------------------------------------- | -------- | ------- |
| id   | path       | A unique integer value identifying this user. | Yes      | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200  |             |

##### Security

| Security Schema | Scopes |
| --------------- | ------ |
| cookieAuth      |        |
| basicAuth       |        |

#### PATCH

##### Parameters

| Name | Located in | Description                                   | Required | Schema  |
| ---- | ---------- | --------------------------------------------- | -------- | ------- |
| id   | path       | A unique integer value identifying this user. | Yes      | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200  |             |

##### Security

| Security Schema | Scopes |
| --------------- | ------ |
| cookieAuth      |        |
| basicAuth       |        |

#### DELETE

##### Parameters

| Name | Located in | Description                                   | Required | Schema  |
| ---- | ---------- | --------------------------------------------- | -------- | ------- |
| id   | path       | A unique integer value identifying this user. | Yes      | integer |

##### Responses

| Code | Description      |
| ---- | ---------------- |
| 204  | No response body |

##### Security

| Security Schema | Scopes |
| --------------- | ------ |
| cookieAuth      |        |
| basicAuth       |        |
