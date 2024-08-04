import ChatUiComponent from "@/components/parts/chat";
import ChatSidePanelComponent from "@/components/parts/side-panel";

export default function Home() {
    return (
        <main className="grid grid-cols-3 gap-4 w-full h-full">
            <div className={"col-span-1 flex flex-col justify-between space-y-2"}>
                <ChatUiComponent/>
            </div>
            <div className={"col-span-2 flex flex-col-reverse justify-items-stretch"}>
                <ChatSidePanelComponent/>
            </div>
        </main>
    );
}