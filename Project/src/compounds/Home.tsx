import { useNavigate } from "react-router-dom"
import RandomJoke from "./RandomJoke";
function Home() {
    const navigate = useNavigate();
    return (
        <>
            <div>
                <h1>Welcome to the place where you will take inspiration from the greatest poets.</h1>
                <p>and after 5 minutes lie on the couch and watch YouTube and forget about it </p>
                <div className="navbar">
                    <br />
                    <button className="buttonGetQuote" onClick={() => { navigate('/quote') }}>For a random quotes click here</button>
                </div>
                <RandomJoke/>
            </div>


        </>
    )
}

export default Home
