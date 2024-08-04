import ChatUiComponent from "@/components/parts/chat-ui";
import ChatSidePanelComponent from "@/components/parts/side-panel";
import {Skeleton} from "@/components/ui/skeleton";

export default function Home() {
    return (
        <main className="grid grid-cols-3 gap-4 w-full h-full">
            <div className={"col-span-1 flex flex-col justify-between space-y-2"}>
                <div className={"bg-slate-950 h-full flex flex-col-reverse space-y-2"}>
                    <Skeleton className="w-full h-[20px] rounded-full"/>
                    <Skeleton className="w-full h-[20px] rounded-full"/>
                    <Skeleton className="w-full h-[20px] rounded-full"/>
                    <Skeleton className="w-full h-[20px] rounded-full"/>
                </div>
                <ChatUiComponent/>
            </div>
            <div className={"col-span-2 flex flex-col-reverse justify-items-stretch"}>
                <ChatSidePanelComponent/>
            </div>
        </main>
    );
}