import axios from "axios";
import React, { useEffect, useState } from "react"

function MakeRubric() {
    const [data, setData] = useState(null);
    const [error, setError] = useState("");
    const [loaded, setLoaded] = useState(false);


    function handleSubmit(e) {
        e.preventDefault();
        const loginForm = e.currentTarget;
        const form = new FormData();
        form.append("rubirc", loginForm.rubirc_name.value)

        console.log(form)
        axios
            .post('http://127.0.0.1:8000/api/rubrics/', form, {"Content-Type": "application/json", })
            .then((response) => setData(response.data))
            .catch((error) => alert('Рубрика с таким названием уже существует'))
            .finally(() => setLoaded(true));

        }

    return (
            <div>
                <form id="make_rubric" onSubmit={handleSubmit}>
                    <label className="form-label">Введите название рубрики для создания новой</label>
                    <input type="text" className="form-control" id="rubirc_name" placeholder="Введите название рубрики"/>

                    <button type="submit" className="btn mainButton">Создать</button>
                </form>
                { data ? (<p>Создана рубрика {data.rubirc}</p>) : (<p></p>)}
            </div>
    )

    
         
}
export default MakeRubric