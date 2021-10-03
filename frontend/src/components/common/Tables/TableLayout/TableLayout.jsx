import TableHeader from "../TableHeader/TableHeader";
import TableBody from "../TableBody/TableBody";
import { StyledTable } from "./css";

export default function TableLayout({ columnNames, columnValues }) {
  return (
    <StyledTable>
      <thead>
        <TableHeader columnNames={columnNames} />
      </thead>
      <tbody>
        <TableBody columnNames={columnNames} columnValues={columnValues} />
      </tbody>
    </StyledTable>
  );
}
