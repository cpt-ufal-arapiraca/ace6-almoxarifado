import { BrowserRouter, Route, Routes, Navigate } from "react-router-dom";
import HomeAlmoxADM from "./pages/HomeAlmoxADM";
import HomeAlmoxCliente from "./pages/HomeAlmoxCliente";



function AppRouter() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="homealmoxadm" element={<HomeAlmoxADM />} />
                <Route path="homealmoxcliente" element={<HomeAlmoxCliente />} />
                <Route path="/" element={<Navigate to="/homealmoxadm" />} />
                <Route path="*" element={<div>404 Not Found</div>} />
            </Routes>
        </BrowserRouter>
    );
}

export default AppRouter;
