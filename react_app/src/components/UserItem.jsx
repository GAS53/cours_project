import React from "react";
import { togleStatus } from "./postService";

const UserItem = ({ userItem }) => {

    console.log(togleStatus)

    function togleHandler(e) {
        togleStatus(userItem.id)
            .then(res => {
                    alert(`Статус пользователя изменен ${userItem.login}`)
                })
            .catch((error) => {
                if (error.response.status === 423 ) {
                        alert(`вы вышли из команды ${userItem.login}`)
                    } else {
                    alert(`Ошибка изменения статуса  ${error.message}`)}})
    }

    return (

        <div class="container-fluid">
            <div class="row justify-content-center align-items-center g-2">

                <div class="col">{userItem.login}</div>
                <div class="col">{userItem.email}</div>
                <div class="col">{userItem.is_active ? "✅" : '❌'}</div>
                <div class="col">
                    {userItem.is_active ?
                        <button type="button" onClick={togleHandler} className="btn btn-outline-danger">
                            Заблокировать
                        </button>
                        :
                        <button type="button" onClick={togleHandler} className="btn btn-outline-success">
                            Разблокировать
                        </button>
                    }

                </div>

            </div>
        </div>

    )
}

export default UserItem