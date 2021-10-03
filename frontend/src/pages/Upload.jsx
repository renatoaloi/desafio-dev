import { ToastContainer, toast } from "react-toastify";
import { Upload as Component } from "../components/Upload/Upload";
import "react-toastify/dist/ReactToastify.css";

export default function Upload({ onInvalidateQuery }) {
  const notify = (msg) => toast(msg);

  return (
    <>
      <Component onInvalidateQuery={onInvalidateQuery} onNotify={notify} />
      <ToastContainer />
    </>
  );
}
