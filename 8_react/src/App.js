import React from 'react';
import './App.css';
import CourseList from "./components/course-list/CourseList";
import {BrowserRouter as Router, Route, Switch} from "react-router-dom";
import About from "./components/about-view/About";
import Navbar from "react-bootstrap/Navbar";
import Nav from "react-bootstrap/Nav";
import 'bootstrap/dist/css/bootstrap.min.css';
import './index.css'
import Row from "react-bootstrap/Row";
import Container from "react-bootstrap/Container";
import Col from "react-bootstrap/Col";
import 'typeface-roboto';
import LoginView from "./components/auth-views/LoginView";
import SignupView from "./components/auth-views/SignUpView";
import CourseListAll from "./components/course-list/CourseListAll";
import CourseListMy from "./components/course-list/CourseListMy";
import LoginControl from "./components/auth-views/LoginControl";


function App() {
    return (
        <Router>
            <Navbar bg="dark" variant="dark">
                <Navbar.Brand>Coursera</Navbar.Brand>
                <Nav className="mr-auto">
                    <Nav.Link href="/">Courses</Nav.Link>
                    {localStorage.token&&<Nav.Link href="/mycourses">My courses</Nav.Link>}
                    <Nav.Link href="/about">About</Nav.Link>
                </Nav>
                <Nav>
                    <LoginControl/>
                </Nav>
            </Navbar>
            <Container>
                <Row>
                    <Col><Switch>
                        <Route path="/about">
                            <About/>
                        </Route>
                        <Route path="/login">
                            <LoginView/>L
                        </Route>
                        <Route path="/signup">
                            <SignupView/>
                        </Route>
                        <Route path="/mycourses">
                            <CourseListMy/>
                        </Route>
                        <Route path="/">
                            <CourseListAll/>
                        </Route>
                    </Switch></Col>
                </Row>
            </Container>
        </Router>
    );
}

export default App;
