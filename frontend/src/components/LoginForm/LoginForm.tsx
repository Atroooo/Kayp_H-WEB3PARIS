import { Label } from "@/components/ui/label";
import { Checkbox } from "@/components/ui/checkbox";
import { Button } from "@/components/ui/button";
import {
    useForm,
    SubmitHandler,
    FieldValues,
    UseFormRegister,
    FormState,
} from "react-hook-form";

export type LoginFormValues = {
    email: string;
    password: string;
};

export interface LoginFormProps {
    onSubmit: SubmitHandler<FieldValues>; // onSubmit function
    register: ReturnType<typeof useForm>["register"]; // register function
    handleSubmit: ReturnType<typeof useForm>["handleSubmit"]; // handleSubmit function
    errors: FormState<FieldValues>["errors"]; // errors object
    watch: ReturnType<typeof useForm>["watch"]; // watch function
}

function EmailField({
    register,
}: {
    register: UseFormRegister<LoginFormValues>;
}): JSX.Element {
    return (
        <div className="flex justify-between items-center">
            <Label htmlFor="email">Email address</Label>
            <input
                {...register("email", {
                    required: "Email is required",
                    pattern: {
                        value: /^\S+@\S+$/,
                        message: "Invalid email address",
                    },
                })}
                type="email"
                id="email"
                className="border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:border-blue-500"
            />
        </div>
    );
}

function PasswordField({
    register,
}: {
    register: UseFormRegister<LoginFormValues>;
}): JSX.Element {
    return (
        <div className="">
            <div className="flex justify-between items-center">
                <Label htmlFor="password">Password</Label>
                <input
                    {...register("password", {
                        required: "Password is required",
                    })}
                    type="password"
                    id="password"
                    className="border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:border-blue-500"
                />
            </div>
            <a className="flex justify-end text-sm underline mt-2" href="#">
                Forgot your password?
            </a>
        </div>
    );
}

function RememberMeCheckbox(): JSX.Element {
    return (
        <div className="flex items-center">
            <Checkbox id="remember-me" className=" border-cyan-500" />
            <Label className="ml-2" htmlFor="remember-me">
                Remember me
            </Label>
        </div>
    );
}

function LoginSubmitButton(): JSX.Element {
    return (
        <Button className="w-full bg-cyan-500" type="submit">
            Login
        </Button>
    );
}

export default function LoginForm({
    onSubmitFormData,
}: {
    onSubmitFormData: (data: LoginFormValues) => void;
}) {
    const { register, handleSubmit } = useForm<LoginFormValues>();
    const onSubmit: SubmitHandler<LoginFormValues> = (data) =>
        onSubmitFormData(data);

    return (
        /* "handleSubmit" will validate your inputs before invoking "onSubmit" */
        <form
            onSubmit={handleSubmit(onSubmit)}
            className=" flex flex-col gap-6"
        >
            <EmailField register={register} />
            <PasswordField register={register} />
            <RememberMeCheckbox />
            <LoginSubmitButton />
        </form>
    );
}
