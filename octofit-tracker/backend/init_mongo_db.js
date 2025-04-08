// MongoDB initialization script for octofit_db
db = connect("localhost:27017/octofit_db");

// Create users collection with unique email index
db.createCollection("users");
db.users.createIndex({ "email": 1 }, { unique: true });

// Create teams collection
db.createCollection("teams");

// Create activity collection
db.createCollection("activity");

// Create leaderboard collection
db.createCollection("leaderboard");

// Create workouts collection
db.createCollection("workouts");

// Insert sample data to ensure collections are persisted
db.users.insertOne({ "email": "sampleuser@example.com", "name": "Sample User" });
db.teams.insertOne({ "name": "Sample Team" });
db.activity.insertOne({ "type": "Sample Activity", "duration": 30 });
db.leaderboard.insertOne({ "user": "sampleuser@example.com", "score": 100 });
db.workouts.insertOne({ "name": "Sample Workout", "calories": 200 });

print("Database and collections initialized successfully.");
