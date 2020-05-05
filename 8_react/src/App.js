import React from 'react';
import './App.css';
import CourseList from "./components/course-list/CourseList";
import CourseDetails from "./components/course-details/CourseDetails";

function App() {
    return (
        <div className="App">
            <h1>Coursera</h1>
            <CourseList/>
        </div>
    );
}

export default App;
