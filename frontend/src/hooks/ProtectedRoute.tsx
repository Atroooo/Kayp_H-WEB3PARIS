import { Navigate, Outlet } from "react-router-dom";

const ProtectedRoute = ({
    isAllowed,
    redirectPath = "/",
    children,
}: {
    isAllowed: boolean;
    redirectPath: string;
    children: React.ReactElement[] | React.ReactElement;
}) => {
    if (!isAllowed) {
        return <Navigate to={redirectPath} replace />;
    }
    return children ? children : <Outlet />;
};

export default ProtectedRoute;
