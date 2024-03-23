import { LoginFormValues } from "@/components/LoginForm/LoginForm";

async function getCsrfToken(): Promise<string> {
    return fetch("http://localhost:8000/authentication/get-csrf-token/", {
        method: "GET",
        credentials: "include",
    })
        .then((response) => response.json())
        .then((data) => {
            return data.csrfToken;
        })
        .catch((error) => {
            console.error("Failed to get CSRF token", error);
            throw error;
        });
}

async function login(
    email: string,
    password: string,
    setIsConnected: (connectingState: boolean) => void
): Promise<void> {
    const csrfToken = await getCsrfToken();

    await fetch("http://localhost:8000/authentication/login/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrfToken,
        },
        credentials: "include",
        body: JSON.stringify({
            email: email,
            password: password,
        }),
    })
        .then((response) => response.json())
        .then(() => {
            setIsConnected(true);
            return;
        })
        .catch((error) => {
            console.error("Error during login fetch:", error);
        });
}

export function handleLoginFormSubmit(
    data: LoginFormValues,
    setIsConnected: (connectingState: boolean) => void
): void {
    if (!data.email || !data.password) {
        return;
    }
    login(data.email, data.password, setIsConnected);
}
