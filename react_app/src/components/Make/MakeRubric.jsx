import axios from "axios";
import React, { useEffect, useState } from "react"
import { createRubric } from '../postService'

function MakeRubric() {
    const [data, setData] = useState(null);

    function handleSubmit(e) {
        e.preventDefault();
        const loginForm = e.currentTarget;
        const form = new FormData();
        form.append("rubirc_name", loginForm.rubirc_name.value)
        console.log(form)
        createRubric(form)
            .then((response) => setData(response.data.rubirc_name))
            .catch((error) => {
                if (error.response.status === 304) {
                    alert('Такая рубрика уже существует')
                } else {
                    alert('Ошибка сервера') 
                }})
        }

    return (
            <div>
                <form id="make_rubric" onSubmit={handleSubmit}>
                    <label className="form-label">Введите название рубрики для создания новой</label>
                    <input type="text" className="form-control" id="rubirc_name" placeholder="Введите название рубрики"/>

                    <button type="submit" className="btn mainButton">Создать</button>
                </form>
                { data ? (<p>Создана рубрика {data}</p>) : (<p></p>)}
            </div>
    )   
}
export default MakeRubric