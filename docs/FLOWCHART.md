# Application Flow

Start
  |
  v
Open Application
  |
  v
Login
  |
  +---- Invalid ----> Show Error ----> Login
  |
 Valid
  |
  v
Dashboard
  |
  +---- Request Resource ----> Save to Database
  |
  +---- Add Resource -------> Save to Database
  |
  +---- View Requests ------> Read Database
  |
  +---- Update Status ------> Update Database
  |
  v
Logout
  |
  v
End
