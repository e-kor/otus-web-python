import React from 'react';
import Button from '@material-ui/core/Button';
import {TextValidator, ValidatorForm} from 'react-material-ui-form-validator';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import APIService from "../APIservice";
import "./UserForm.css"

class UserForm extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            username: "",
            password: ""
        };
        this.apiService = new APIService();
    }

    handleUsernameChange = (event) => {
        // const email = event.target.value;
        // console.log(event.target);
        this.setState({username: event.target.value});
    }

    handlePasswordChange = (event) => {
        // const email = event.target.value;
        // console.log(event.target);
        this.setState({password: event.target.value});
    }

    handleSubmit = () => {
        console.log(this.state);
        this.props.handleSubmit(this.state)
    }

    render() {
        const {username, password} = this.state;
        return (

            <ValidatorForm
                ref="form"
                onSubmit={this.handleSubmit}
                onError={errors => console.log(errors)}
            ><Typography component="h1" variant="h5">
                {this.props.headerText}
            </Typography>
                <Grid container spacing={2}>
                    <Grid item xs={12}>
                        <TextValidator
                            label="Username"
                            onChange={this.handleUsernameChange}
                            name="username"
                            value={username}
                            validators={['required']}
                            errorMessages={['this field is required']}
                            variant="outlined"
                            required
                            fullWidth
                        />
                    </Grid>
                    <Grid item xs={12}>
                        <TextValidator
                            label="Password"
                            onChange={this.handlePasswordChange}
                            name="password"
                            value={password}
                            validators={['required']}
                            errorMessages={['this field is required']}
                            variant="outlined"
                            type="password"
                            required
                            fullWidth
                        />
                    </Grid>

                    <Button
                        type="submit"
                        fullWidth
                        variant="contained"
                        color="primary"
                    >
                        {this.props.buttonText}
                    </Button>

                </Grid>
            </ValidatorForm>
        );
    }
}

UserForm.defaultProps = {
    headerText: "Login",
    buttonText: "GO",
    handleSubmit(data) {
        console.log(data)
    }
}
export default UserForm;
