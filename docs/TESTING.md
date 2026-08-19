# Testing Plan

| Test Case | Input | Expected Result |
|---|---|---|
| Login valid | admin@example.com / admin123 | Dashboard opens |
| Login invalid | wrong password | Error shown |
| Add resource | Water, 100, Chennai | Resource appears |
| Request resource | Food, 20, Chennai, High | Request appears |
| Update status | Approved | Status changes |
| Logout | Click Logout | Login page opens |
| API | GET /api/requests while logged in | JSON request list |
| Docker | Open localhost:5000 | Application loads |

## Testing Types

- Functional testing
- Integration testing
- UI testing
- API testing
- Docker deployment testing
