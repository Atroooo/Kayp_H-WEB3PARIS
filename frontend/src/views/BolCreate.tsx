import {PageLayout} from "@/components/Bol/PageLayout.tsx";
import {BolCreateForm} from "@/components/Bol/BolCreateForm.tsx";


export const BolCreate = () => {
    return (
        <div className={"flex w-full"}>
            <PageLayout title={"Create a eBL"}>
                <BolCreateForm />
            </PageLayout>

        </div>
    );
}