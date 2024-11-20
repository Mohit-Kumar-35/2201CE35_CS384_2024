import pandas as pd

input_file_path = 'Input-1 Lab 10.xlsx'
input_df = pd.read_excel(input_file_path)

# Extract max marks and weightage from the first two rows
max_marks = input_df.iloc[0, 2:6].astype(float)  # Max marks for Mid Sem, Endsem, Quiz 1, Quiz 2
weightage = input_df.iloc[1, 2:6].astype(float)  # Weightage for each component
# print(max_marks)
# print(weightage)
# Function to calculate 'Grand Total/100' for each student row
def calculate_grand_total(row):
    return ((row['Mid Sem'] / max_marks['Mid Sem']) * weightage['Mid Sem'] +
            (row['Endsem'] / max_marks['Endsem']) * weightage['Endsem'] +
            (row['Quiz 1'] / max_marks['Quiz 1']) * weightage['Quiz 1'] +
            (row['Quiz 2'] / max_marks['Quiz 2']) * weightage['Quiz 2'])

# Filter rows with missing names and separate them
students_with_names = input_df[input_df['Name'].notna()]
students_without_names = input_df[input_df['Name'].isna()]

# print(input_df.head(5));

# Apply the function to each student's row (skip the first two rows)
students_with_names['Grand Total/100'] = students_with_names.apply(calculate_grand_total, axis=1)

# print(students_with_names['Grand Total/100']);

# Sort  by 'Grand Total/100' in descending order
students_with_names = students_with_names.sort_values(by='Grand Total/100', ascending=False).reset_index(drop=True)

# Function to assign grades based on percentile ranges
def assign_grade_based_on_percentile(index, total_students):
    percentile = (index + 1) / total_students * 100  # Calculate percentile rank

    if percentile <= 5:
        return 'AA'
    elif percentile <= 20:
        return 'AB'
    elif percentile <= 45:
        return 'BB'
    elif percentile <= 75:
        return 'BC'
    elif percentile <= 90:
        return 'CC'
    elif percentile <= 95:
        return 'CD'
    elif percentile <= 100:
        return 'DD'

# Apply the grade function to each student's row
# students_with_names['Grade'] = students_with_names.index.to_series().apply(lambda x: assign_grade_based_on_percentile(x, len(students_with_names)))
students_with_names['Grade'] = students_with_names.index.to_series().apply(
    assign_grade_based_on_percentile, total_students=len(students_with_names)
)
# Concatenate the students with names and students without names, keeping students without names at the top
final_df = pd.concat([students_without_names, students_with_names], ignore_index=True)

first_three_rows=final_df.iloc[:2];
remaining_rows=final_df.iloc[2:];
remaining_rows=remaining_rows.sort_values(by='Roll').reset_index(drop=True);

# print(remaining_rows.head(5));
final_df2=pd.concat([first_three_rows,remaining_rows],ignore_index=True);


with pd.ExcelWriter('output.xlsx', engine='openpyxl') as writer:
    # Write first sheet (df1)
    final_df.to_excel(writer, sheet_name='Sheet1_Grade_Sorted', index=False)

    # Write second sheet (df2)
    final_df2.to_excel(writer, sheet_name='Sheet2_Roll_Sorted', index=False)



# print(f"The sorted output has been saved to {output_path1}")