export default function TableHeader({ columnNames }) {
  return (
    <tr>
      {columnNames.map((columnName, k) => (
        <th
          style={{ borderBottomStyle: "solid", borderBottomWidth: "1px" }}
          key={k}
        >
          {columnName}
        </th>
      ))}
    </tr>
  );
}
