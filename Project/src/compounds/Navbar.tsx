
import { NavLink } from "react-router-dom";
function Navbar() {
    const activeStyle = {
        fontWeight: "bold",
        color: "blue",
    };
    interface ComponentProps {
        isActive: boolean;      
    }
    return (
        <>
            <nav className="navbar">
                <NavLink to="/app-quotes/" style={({ isActive }: ComponentProps) => (isActive ? activeStyle : undefined)}>Home</NavLink> {' '}| {' '}
                <NavLink to="/quote" style={({ isActive }:ComponentProps) => (isActive ? activeStyle : undefined)}>Quotes</NavLink> 
            </nav>

        </>
    )
}

export default Navbar
