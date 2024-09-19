const data = fs.readFileSync(path, 'utf8');
    
    // Split the data into lines and filter out empty lines
    const lines = data.split('\n').filter(line => line.trim() !== '');
    
    // Remove the header line
    const students = lines.slice(1);
    
    console.log(`Number of students: ${students.length}`);
    
    // Create an object to store students by field
    const fieldCounts = {};
    const fieldStudents = {};
    
    students.forEach(student => {
      const [firstname, lastname, age, field] = student.split(',');
      if (!fieldCounts[field]) {
        fieldCounts[field] = 0;
        fieldStudents[field] = [];
      }
      fieldCounts[field]++;
      fieldStudents[field].push(firstname);
    });
    
    // Log the count and list of students for each field
    for (const field in fieldCounts) {
      console.log(`Number of students in ${field}: ${fieldCounts[field]}. List: ${fieldStudents[field].join(', ')}`);
    }
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
