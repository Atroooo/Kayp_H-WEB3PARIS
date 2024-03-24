import { Routes, Route, BrowserRouter } from "react-router-dom";
import ProtectedRoute from "@/hooks/ProtectedRoute.tsx";
import Sidebar2 from "@/components/navigation/Sidebar.tsx";
import Login from "./views/Login";
import { BolCreate } from "@/views/BolCreate.tsx";
import { Layout } from "@/components/custom/Layout.tsx";
import { BolSuccess } from "@/views/BolSuccess.tsx";
import { ListOfDocuments } from "./views/ListOfDocuments";
import {
    isConnectedStore,
    IsConnectedStoreInterface,
} from "./hooks/isConnected";

function App() {
    const { isConnected } = isConnectedStore() as IsConnectedStoreInterface;

    const loginFallback = "/log-in";
    return (
        <>
            <BrowserRouter>
                <Routes>
                    <Route
                        path={loginFallback}
                        element={
                            <ProtectedRoute
                                isAllowed={!isConnected}
                                redirectPath={"/"}
                            >
                                <Login />
                            </ProtectedRoute>
                        }
                    ></Route>

                    <Route>
                        <Route
                            path="/"
                            element={
                                <ProtectedRoute
                                    isAllowed={isConnected}
                                    redirectPath={loginFallback}
                                >
                                    <Sidebar2 />
                                    <div>Dashboard</div>
                                </ProtectedRoute>
                            }
                        ></Route>

                        <Route
                            path="/bol/create"
                            element={
                                <ProtectedRoute
                                    isAllowed={isConnected}
                                    redirectPath={loginFallback}
                                >
                                    <Layout className={"flex-row gap-2"}>
                                        <Sidebar2 />
                                        <BolCreate />
                                    </Layout>
                                </ProtectedRoute>
                            }
                        ></Route>

                        <Route
                            path="/bol/success"
                            element={
                                <ProtectedRoute
                                    isAllowed={isConnected}
                                    redirectPath={loginFallback}
                                >
                                    <Layout className={"flex-row gap-2"}>
                                        <Sidebar2 />
                                        <BolSuccess />
                                    </Layout>
                                </ProtectedRoute>
                            }
                        ></Route>

                        <Route
                            path="/bol/list"
                            element={
                                <ProtectedRoute
                                    isAllowed={isConnected}
                                    redirectPath={loginFallback}
                                >
                                    <Layout className={"flex-row gap-2"}>
                                        <Sidebar2 />
                                        <ListOfDocuments />
                                    </Layout>
                                </ProtectedRoute>
                            }
                        ></Route>

                        <Route
                            path="/bol/draft"
                            element={
                                <ProtectedRoute
                                    isAllowed={isConnected}
                                    redirectPath={loginFallback}
                                >
                                    <Sidebar2 />
                                    <div>Draft</div>
                                </ProtectedRoute>
                            }
                        ></Route>

                        <Route
                            path="/activity/notifications"
                            element={
                                <ProtectedRoute
                                    isAllowed={isConnected}
                                    redirectPath={loginFallback}
                                >
                                    <Sidebar2 />
                                    <div>Notifications</div>
                                </ProtectedRoute>
                            }
                        ></Route>

                        <Route
                            path="/activity/history"
                            element={
                                <ProtectedRoute
                                    isAllowed={isConnected}
                                    redirectPath={loginFallback}
                                >
                                    <Sidebar2 />
                                    <div>History</div>
                                </ProtectedRoute>
                            }
                        ></Route>

                        <Route
                            path="/settings"
                            element={
                                <ProtectedRoute
                                    isAllowed={isConnected}
                                    redirectPath={loginFallback}
                                >
                                    <Sidebar2 />
                                    <div>Settings</div>
                                </ProtectedRoute>
                            }
                        ></Route>
                    </Route>
                </Routes>
            </BrowserRouter>
        </>
    );
}

export default App;
