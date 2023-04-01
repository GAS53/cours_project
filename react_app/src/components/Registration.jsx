import { Button } from "./UI/button/Button";
import React, { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";


const Registration = () => {
    const navigate = useNavigate();
    const [validated, setValidated] = useState(false);
    const [form, setForm] = useState({});
    const [error, setError] = useState(null);

    const handleSubmit = (event) => {
        event.preventDefault();
        const registrationForm = event.currentTarget;
        if (registrationForm.checkValidity() === false) {
        event.stopPropagation();
        }
        setValidated(true);
        const data = {
            username: registrationForm.username.value,
            surname: registrationForm.username.value,
            first_name: registrationForm.first_name.value,
            password: registrationForm.password.value,
            email: registrationForm.email.value,
            age: registrationForm.age.value,
            };
        console.log('data')
        console.log(data)
        axios.post("http://127.0.0.1:8000/api/register/",  data)
            .then((res) => {
                console.log('res')
                console.log(res)
                localStorage.setItem("auth", JSON.stringify({
                    access: res.data.access,
                    refresh: res.data.refresh,
                    user: res.data.user,
                }));
                navigate("/");
            })
            .catch((err) => {
                if (err.message) {
                setError(err.request.response);
                }
            });
    }
                    
    return (
        <div className="container-md mt-5">
            <div className="row justify-content-center align-items-top">
                <div className="col-8">

                    <form
                        id="registration-form"
                        noValidate
                        validated={validated.toString()}
                        onSubmit={handleSubmit}
                        >

                        <div className="form-file">
                            <input type="file" className="form-file-input btn btn-outline-primary" id="customFile"/>
                        </div>

                        <div className="mb-3">
                            <label className="form-label">Логин</label>
                            <input type="text" className="form-control" id="username" placeholder="Введите ваш логин"/>
                        </div>

                        <div className="mb-3">
                            <label className="form-label">Имя</label>
                            <input type="text" className="form-control" id="first_name"
                                placeholder="Введите Ваше имя"/>
                        </div>

                        <div className="mb-3">
                            <label className="form-label">Фамилия</label>
                            <input type="text" className="form-control" id="surname" placeholder="Введите вашу фамилию"/>
                        </div>

                        <div className="mb-3">
                            <label className="form-label">Возраст</label>
                            <input type="number" className="form-control" id="age" placeholder="Сколько вам лет"/>
                        </div>

                        <div className="mb-3">
                            <label  className="form-label">Адрес почты</label>
                            <input type="email" className="form-control" id="email" aria-describedby="emailHelp"
                                placeholder="Ваш@email.com"/>
                            <div id="emailHelp" className="form-text">Мы никогда никому не передадим вашу электронную почту.
                            </div>
                        </div>

                        <div className="mb-3">
                            <label  className="form-label">Пароль</label>
                            <input type="password" className="form-control" id="password"/>
                            <div id="passwordHelpBlock" className="form-text">
                                Ваш пароль должен состоять из 8-20 символов, содержать буквы и цифры и не должен
                                содержать пробелов, специальных символов или эмодзи.
                            </div>
                        </div>

                        <Button text="Зарегистрироваться" styles="mainButton"/>
                    </form>
                </div>
            </div>
        </div>
    );
};

export default Registration;