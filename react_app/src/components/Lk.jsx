import React from "react";
import { RowTwoValues } from "./UI/rows/RowTwoValues";
import { getUserInfo } from "./Auth";


const Lk = ({ user }) => {
    const userInfo = getUserInfo()
    console.log('userInfo')
    console.log(userInfo)
    // const elements = [
    //     [
    //         {
    //             title: "Никнейм",
    //             data: user.nickname,

    //         },
    //         {
    //             title: "Дата регистраци",
    //             data: user.registrationdate,
    //         }
    //     ],
    //     [
    //         {
    //             title: "Имя",
    //             data: user.username,

    //         },
    //         {
    //             title: "Фамилия",
    //             data: user.surname,
    //         }
    //     ],
    //     [
    //         {
    //             title: "Адрес почты",
    //             data: user.email,

    //         },
    //         {
    //             title: "Возраст",
    //             data: user.age,
    //         }
    //     ]
    // ];

    return (
        <div className="container-md mt-5">
            <div className="row justify-content-center align-items-top">

                <div className="col-4">
                    <img src={user.avatar}
                        className="img-fluid img-thumbnail rounded" alt="Аватар" />
                    <h3>{user.nickname}</h3>
                </div>

                <div className="col-8">
                    {/* {
                        elements.map((values, index) => <RowTwoValues values={values} key={index}/>)
                    } */}
                </div>
            </div>
        </div>
    );
};

export default Lk;