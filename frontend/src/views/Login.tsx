import { CardHeader, CardContent, Card } from "@/components/ui/card";

import { handleLoginFormSubmit } from "@/services/loginService";
import LoginForm, { LoginFormValues } from "@/components/LoginForm/LoginForm";

function LoginComponentHeader() {
    return (
        <CardHeader className="space-y-1">
            <img src="color_logo_black_name_no_bg.svg" alt="Logo" />
        </CardHeader>
    );
}

function LoginComponentContent() {
    const handleLogin = (data: LoginFormValues) => {
        handleLoginFormSubmit(data);
        console.log(data);
    };

    return (
        <CardContent>
            <LoginForm onSubmitFormData={handleLogin} />
        </CardContent>
    );
}

export default function Login() {
    return (
        <div className="flex justify-center items-center h-screen">
            <Card className="max-w-sm">
                <LoginComponentHeader />
                <LoginComponentContent />
            </Card>
        </div>
    );
}
