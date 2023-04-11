import axios from "axios";
import React, { useEffect, useState } from "react"

function MakeRubric() {
    const [data, setData] = useState(null);
    const [error, setError] = useState("");
    const [loaded, setLoaded] = useState(false);


    console.log('sendData')
    function handleSubmit(e) {
        e.preventDefault();
        const loginForm = e.currentTarget;
        const form = new FormData();
        form.append("rubirc_name", loginForm.rubirc_name.value)

        console.log(form)
        axios
            .post('http://127.0.0.1:8000/api/rubrics/', form, {"Content-Type": "application/json", })
            .then((response) => setData(response.data))
            .catch((error) => setError(error.message))
            .finally(() => setLoaded(true));

        }

    return (
            <form id="make_rubric" onSubmit={handleSubmit}>
                <label className="form-label">Рубрика</label>
                <input type="text" className="form-control" id="rubirc_name" placeholder="Введите название рубрики"/>

                <button type="submit" className="btn mainButton">Создать</button>
            </form>
    )

    
         
}
export default MakeRubric