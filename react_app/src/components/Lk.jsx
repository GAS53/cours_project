import React, { useEffect, useState } from "react";
import { RowTwoValues } from "./UI/rows/RowTwoValues";
import { getUserInfo } from "./Auth";
import { useParams } from "react-router-dom";
import axios from "axios";

import { useNavigate } from "react-router-dom";


const Lk = (props) => {
    const [im, setIm] = useState([])


    useEffect(() => {
        const auth = JSON.parse(localStorage.getItem('auth'))
        console.log('111111')
        console.log(auth)
        const user = auth.user
        if (auth) {

            const data = [
                    [ { title: "Никнейм", data: user.login, },],
                    [ { title: "Имя", data: user.first_name,},],
                    [ { title: "Фамилия",  data: user.last_name, } ],
                    [ { title: "Адрес почты",  data: user.email,},],
                    [ { title: "Возраст",  data: user.age, } ],
                ]
            setIm(data)
        }
       
      }, [setIm]);


    return (
        <div className="container-md mt-5">
            <div className="row justify-content-center align-items-top">

                <div className="col-4">
                    <img src={im.avatar}
                        className="img-fluid img-thumbnail rounded" alt="Аватар" />
                    <h3>{im.username}</h3>
                </div>
                <div className="col-8">
                    {
                        im.map((values, index) => <RowTwoValues values={values} key={index}/>)
                    }
                </div>
            </div>
        </div>
    );
};

export default Lk;