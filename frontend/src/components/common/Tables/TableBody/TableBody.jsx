import { StyledColumn } from "./css";

export default function TableBody({ columnNames, columnValues }) {
  console.log("columnNames", columnNames);
  console.log("columnValues", columnValues);
  return (
    <>
      {columnValues.map((columnValue, ck) => (
        <tr key={ck}>
          {columnNames.map((_, k) => (
            <StyledColumn key={k}>{String(columnValue[k])}</StyledColumn>
          ))}
        </tr>
      ))}
    </>
  );
}
