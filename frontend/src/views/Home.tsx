import { Terminal } from "lucide-react"

import {
    Alert,
    AlertDescription,
    AlertTitle,
} from "@/components/ui/alert"
export const Home = () => {

    return (
        <div>
            <Alert>
                <Terminal className="h-4 w-4" />
                <AlertTitle>Hello</AlertTitle>
                <AlertDescription>
                    <div className={"flex justify-between items-center"}>
                        You can add components to your app using the cli.
                    </div>
                </AlertDescription>
            </Alert>
        </div>
    );
}