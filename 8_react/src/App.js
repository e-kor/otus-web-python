import React from 'react';
import './App.css';
import CourseList from "./components/course-list/CourseList";
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link
} from "react-router-dom";
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
import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import IconButton from "@material-ui/core/IconButton";
import Grid from "@material-ui/core/Grid";


function App() {
    return (
        <Router>

            <Navbar bg="dark" variant="dark">
                <Navbar.Brand href="/">Coursera</Navbar.Brand>
                <Nav className="mr-auto">
                    <Nav.Link href="/">Courses</Nav.Link>
                    <Nav.Link href="/about">About</Nav.Link>
                    <Nav.Link href="/login">Login</Nav.Link>
                    <Nav.Link href="/signup">Signup</Nav.Link>
                </Nav>
            </Navbar>

            <AppBar position="static">
                <Toolbar>

                    <Link href="/login" variant="body2">
                        Login
                    </Link>

                </Toolbar>
            </AppBar>

            <Container>
                <Row>
                    <Col><Switch>
                        <Route path="/about">
                            <About/>
                        </Route>
                        <Route path="/login">
                            <LoginView/>
                        </Route>
                        <Route path="/signup">
                            <SignupView/>
                        </Route>
                        <Route path="/">
                            <CourseList/>
                        </Route>
                    </Switch></Col>
                </Row>
            </Container>


        </Router>
    );
}

export default App;
