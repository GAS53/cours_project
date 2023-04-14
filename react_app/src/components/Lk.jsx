import React, { useEffect, useState } from "react";
import { RowTwoValues } from "./UI/rows/RowTwoValues";
import { loadAuth } from './postService'


const Lk = (props) => {
    const [im, setIm] = useState([])


    useEffect(() => {
        const auth = loadAuth()
        console.log('auth')
        console.log(auth.user)
        if (auth) {
            const data = [
                    [ { title: "Никнейм", data: auth.login, },],
                    [ { title: "Имя", data: auth.first_name,},],
                    [ { title: "Фамилия",  data: auth.last_name, } ],
                    [ { title: "Адрес почты",  data: auth.email,},],
                    [ { title: "Возраст",  data: auth.age, } ],
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