import axios from "axios";
import React, { useEffect, useState } from "react"

function GetRubric() {
    const [data, setData] = useState(null);
    const [error, setError] = useState("");
    const [loaded, setLoaded] = useState(false);


    function getRugrics(e) {
        e.preventDefault();

        axios
            .get('http://127.0.0.1:8000/api/rubrics/', {"Content-Type": "application/json", })
            .then((response) => setData(response.data.results))
            .catch((error) => setError(error.message))
            .finally(() => setLoaded(true));
        }
    console.log(data)
    return (
            <div>
                <form id="make_rubric" onSubmit={handleSubmit}>
                    <label className="form-label">Рубрика</label>
                    <input type="text" className="form-control" id="rubirc_name" placeholder="Введите название рубрики"/>

                    <button type="submit" className="btn mainButton">Создать</button>
                </form>
                { data ? (<p>Создана рубрика {data.rubirc_name}</p>) : (<p></p>)}
            </div>
    )

    
         
}
export default GetRubric