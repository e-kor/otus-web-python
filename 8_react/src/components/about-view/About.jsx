import React from 'react';
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import "./About.css"
import ContactForm from "./ContactForm";

const About = props => {
    return (
        <div>
            <h1>About</h1>
            <div className="about__aboutus"> Кто мы?
                Не знаем!
                Чего мы хотим?
                Всего!
                Когда мы хотим?
                Сейчас!
            </div>
<ContactForm/>
        </div>
    )
};

export default About;
