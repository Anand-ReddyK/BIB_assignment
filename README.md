# BIB_assignment

## To Setup and Run the Project
1. **Clone the Repository**
   
   ```
   git clone https://github.com/Anand-ReddyK/BIB_assignment.git
   ```
2. **Create and Activate a Virtual Environment**

   ```
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. **Install Dependencies**
   ```
   cd .\BIB_assignment\
   pip install -r .\requirements.txt
   ```

4. **Run the project**
   ```
   daphne RealTImeChat.asgi:application
   ```

## Assumptions and Decisions Made During Development

- **Room Access:** I created rooms that can be accessed by all users (universal). Rooms are not restricted, and any authenticated user can join them.
- **Room Creation:** I manually created some rooms and did not implement forms or any feature that allows users to create their own rooms.
- **User Authentication:** I used Django's built-in `User` class for user creation and authentication.

## How to Test the Application

1. **Pre-created Users:**
    - **User 1:**
      - Username: `admin_user`
      - Password: `qwertyuiop`
    - **User 2:**
      - Username: `user1`
      - Password: `G#5w9vZ!k2P@8qXr`

2. **Pre-created Rooms:**
    - Rooms are created in advance and will be visible once logged in.

3. **Testing Steps:**
    - After running the server, open **two web browsers** (or one in incognito mode) to simulate different users.
    - Log in with two different users, one in each browser.
    - You can now:
      - **Send and receive messages** via websockets in real-time.
      - **See active users** in the room by checking the **online section** on the right side of the chat interface.


   
