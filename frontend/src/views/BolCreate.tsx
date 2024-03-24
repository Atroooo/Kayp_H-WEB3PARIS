import {PageLayout} from "@/components/layout/PageLayout.tsx";
import {BolCreateForm} from "@/components/bol/BolCreateForm.tsx";


export const BolCreate = () => {
    return (
        <div className={"flex w-full"}>
            <PageLayout title={"Create a eBL"}>
                <BolCreateForm />
            </PageLayout>

        </div>
    );
}