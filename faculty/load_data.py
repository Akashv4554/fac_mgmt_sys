from faculty.models import FacultyMember

faculty_data = {

    1: {
        'name': 'Dr. Ravi Ram',
        'dept': 'CSE',
        'email': 'raviramv@ssit.edu.in',
        'designation': 'Professor',
        'qualifications': 'M.Tech., Ph.D',
        'specialization': 'Vehicular Ad-Hoc Networks',
        'contact_no': '9845432933',
        'experience': '24 years',
        'img': 'faculty/raviram.jpg'
    },

    2: {
        'name': 'Dr. M Siddappa',
        'dept': 'CSE',
        'email': 'siddappam@ssit.edu.in',
        'designation': 'Professor',
        'qualifications': 'B.E., M.Tech., Ph.D.',
        'specialization': 'Data analysis',
        'contact_no': '9448077405',
        'experience': '35 years',
        'img': 'faculty/Siddappa.jpg'
    },

    3: {
        'name': 'Dr. Guruprakash C D',
        'dept': 'CSE',
        'email': 'cdguruprakash@gmail.com',
        'designation': 'Professor',
        'qualifications': 'B.E., M.Tech., Ph.D.',
        'specialization': 'Computer Networking',
        'contact_no': '9844782445',
        'experience': '32 years',
        'img': 'faculty/guruprasad.jpg'
    },

    4: {
        'name': 'Dr. Sujatha S R',
        'dept': 'CSE',
        'email': 'sujathasr@ssit.edu.in',
        'designation': 'Professor',
        'qualifications': 'B.E., M.E., Ph.D.',
        'specialization': 'Wireless Sensor Network',
        'contact_no': '9986040906',
        'experience': '24 years',
        'img': 'faculty/sujatha.jpg'
    },

    5: {
        'name': 'Dr. Vivek Veeraiah',
        'dept': 'CSE',
        'email': 'Vivek@ssahe.in',
        'designation': 'Professor',
        'qualifications': 'Ph.D.',
        'specialization': 'IoT, Machine Learning',
        'contact_no': '',
        'experience': '10 years',
        'img': 'faculty/vivekveerayya.jpeg'
    },

    6: {
        'name': 'Dr. Asha K R',
        'dept': 'CSE',
        'email': 'ashakr@ssit.edu.in',
        'designation': 'Associate Professor',
        'qualifications': 'M.C.A, M.Phil., M.Tech., Ph.D.',
        'specialization': 'Wireless Sensor Network, Machine Learning, Deep learning',
        'contact_no': '9538104144',
        'experience': '23 years',
        'img': 'faculty/asha.jpg'
    },

    7: {
        'name': 'Dr. Babitha M N',
        'dept': 'CSE',
        'email': 'babithamn@ssit.edu.in',
        'designation': 'Associate Professor',
        'qualifications': 'B.E, M.Tech, Ph.D.',
        'specialization': 'Cloud Computing',
        'contact_no': '9886056815',
        'experience': '24 years',
        'img': 'faculty/babitha.jpg'
    },

    8: {
        'name': 'Dr. Gopala T',
        'dept': 'CSE',
        'email': 'gopalat@ssit.edu.in',
        'designation': 'Associate Professor',
        'qualifications': 'B.E., M.Tech., Ph.D.',
        'specialization': 'Wireless Sensor Network',
        'contact_no': '9886392509',
        'experience': '16.3 years',
        'img': 'faculty/gopala.jpg'
    },

    9: {
        'name': 'Dr. Roopa N K',
        'dept': 'CSE',
        'email': 'roopank@ssit.edu.in',
        'designation': 'Associate Professor',
        'qualifications': 'B.E., M.Tech., Ph.D.',
        'specialization': 'Machine Learning, Data Mining',
        'contact_no': '9900243628',
        'experience': '19 years',
        'img': 'faculty/Roopa.jpg'
    },

    10: {
        'name': 'Dr. NIRMALA G',
        'dept': 'CSE',
        'email': 'nirmalag@ssit.edu.in',
        'designation': 'Associate Professor',
        'qualifications': 'B.E., M.Tech., Ph.D.',
        'specialization': 'Computer Networks, Programming Languages',
        'contact_no': '8971417165',
        'experience': '19 years',
        'img': 'faculty/nirmala.jpg'
    },

    11: {
        'name': 'Bharath T S',
        'dept': 'CSE',
        'email': 'bharathts@ssit.edu.in',
        'designation': 'Associate Professor',
        'qualifications': 'M.Tech.',
        'specialization': 'Web Application',
        'contact_no': '9844734835',
        'experience': '17 years',
        'img': 'faculty/bharath.jpg'
    },

    12: {
        'name': 'Madhumala G',
        'dept': 'CSE',
        'email': 'madhumalag@ssit.edu.in',
        'designation': 'Assistant Professor',
        'qualifications': 'M.Tech.',
        'specialization': 'Cloud computing',
        'contact_no': '8050472311',
        'experience': '18 years',
        'img': 'faculty/madhumala.jpg'
    },

    13: {
        'name': 'Sindhu T N',
        'dept': 'CSE',
        'email': 'sindhutn@ssit.edu.in',
        'designation': 'Assistant Professor',
        'qualifications': 'M.Tech.(Ph.D.)',
        'specialization': 'Data Mining',
        'contact_no': '9141131809',
        'experience': '20 years',
        'img': 'faculty/sindhu.jpg'
    },

    14: {
        'name': 'Swarnalatha G L',
        'dept': 'CSE',
        'email': 'swarnalathagl@ssit.edu.in',
        'designation': 'Assistant Professor',
        'qualifications': 'B.E., M.Tech.',
        'specialization': 'Digital Electronics',
        'contact_no': '9743505707',
        'experience': '15 years',
        'img': 'faculty/swarnalatha.jpg'
    },

    15: {
        'name': 'Veena N D',
        'dept': 'CSE',
        'email': 'veenand@ssit.edu.in',
        'designation': 'Assistant Professor',
        'qualifications': 'M.Tech. (Ph.D.)',
        'specialization': 'Machine Learning',
        'contact_no': '9743641862',
        'experience': '12.6 years',
        'img': 'faculty/Veena.jpg'
    },

    16: {
        'name': 'Prathiba S B',
        'dept': 'CSE',
        'email': 'prathibasb@ssit.edu.in',
        'designation': 'Assistant Professor',
        'qualifications': 'M.Tech(Ph.D.)',
        'specialization': 'Computer Networks',
        'contact_no': '9844860667',
        'experience': '18 years',
        'img': 'faculty/Prathiba.jpg'
    },

    17: {
        'name': 'Bhoomika P',
        'dept': 'CSE',
        'email': 'bhoomikap@ssit.edu.in',
        'designation': 'Assistant Professor',
        'qualifications': 'B.E., M.Tech.',
        'specialization': 'Computer Science & Engg.',
        'contact_no': '8073496905',
        'experience': '5 years',
        'img': 'faculty/bhoomika.jpg'
    },

    18: {
        'name': 'Bharathi N',
        'dept': 'CSE',
        'email': 'bharathinghorpade@gmail.com',
        'designation': 'Assistant Professor',
        'qualifications': 'M.Tech(Ph.D.)',
        'specialization': 'Image Processing',
        'contact_no': '7019796906',
        'experience': '11 years',
        'img': 'faculty/Bharathi.jpeg'
    },

    19: {
        'name': 'Noor Fathima K',
        'dept': 'CSE',
        'email': 'noorfathima_us@yahoo.com',
        'designation': 'Assistant Professor',
        'qualifications': 'B.E., M.Tech.',
        'specialization': 'Image Processing',
        'contact_no': '7022793749',
        'experience': '27 years',
        'img': 'faculty/NoorFathima.jpg'
    },

    20: {
        'name': 'SREEBHARGAVI M',
        'dept': 'CSE',
        'email': 'nayaka.bhargavi85@gmail.com',
        'designation': 'Assistant Professor',
        'qualifications': 'B.E., M.Tech.',
        'specialization': 'Computer Science & Engineering',
        'contact_no': '9902319434',
        'experience': '7.8 years',
        'img': 'faculty/Bhargavi.jpg'
    },

    21: {
        'name': 'Bhagya Jyothi M K',
        'dept': 'CSE',
        'email': 'bjyoti.23@gmail.com',
        'designation': 'Assistant Professor',
        'qualifications': 'B.E., M.Tech.',
        'specialization': 'Network Security, Artificial Intelligence and Machine Learning',
        'contact_no': '8951193710',
        'experience': '8 years',
        'img': 'faculty/Bhagyajyothi.jpg'
    },

    22: {
        'name': 'Shwetha M K',
        'dept': 'CSE',
        'email': 'Shwethacit@gmail.com',
        'designation': 'Assistant Professor',
        'qualifications': 'B.E., M.Tech.',
        'specialization': 'VLSI and Embedded systems',
        'contact_no': '6363234163',
        'experience': '1.6 years',
        'img': 'faculty/shwetha.jpg'
    },

    23: {
        'name': 'Sharath babu C G',
        'dept': 'CSE',
        'email': '',
        'designation': 'Assistant Professor',
        'qualifications': 'BE, M.Tech., (Ph.D.)',
        'specialization': 'VLSI and Embedded systems',
        'contact_no': '9448970162',
        'experience': '2.10 years',
        'img': 'faculty/sharathbabucg.jpg'
    },

    24: {
        'name': 'Thanushree Y',
        'dept': 'CSE',
        'email': 'thanushreey@ssit.edu.in',
        'designation': 'Assistant Professor',
        'qualifications': 'MCA',
        'specialization': 'Artificial Intelligence',
        'contact_no': '8088009879',
        'experience': '1 years',
        'img': 'faculty/thanushree.jpg'
    },

    25: {
        'name': 'Shivakiran N',
        'dept': 'CSE',
        'email': 'shivakirann@ssit.edu.in',
        'designation': 'Assistant Professor',
        'qualifications': 'MCA',
        'specialization': 'Full stack web development',
        'contact_no': '8088783619',
        'experience': 'Fresher',
        'img': 'faculty/shivakiran.jpg'
    },

    26: {
        'name': 'Harshitha T S',
        'dept': 'CSE',
        'email': 'harshithats@ssit.edu.in',
        'designation': 'Assistant Professor',
        'qualifications': 'M.Tech.',
        'specialization': 'Computer Science',
        'contact_no': '9663826347',
        'experience': '1 years',
        'img': 'faculty/harshitha.jpg'
    },

    27: {
        'name': 'Meghana C V',
        'dept': 'CSE',
        'email': 'megha.maduri@gmail.com',
        'designation': 'Assistant Professor',
        'qualifications': 'M.Tech.',
        'specialization': 'Computer Science',
        'contact_no': '8088069820',
        'experience': 'Fresher',
        'img': 'faculty/meghana.jpg'
    },

    28: {
        'name': 'Aishwarya R',
        'dept': 'CSE',
        'email': 'aishwaryar@ssit.edu.in',
        'designation': 'Assistant Professor',
        'qualifications': 'M.Tech',
        'specialization': 'Computer Science and Engineering',
        'contact_no': '9353824594',
        'experience': 'Fresher',
        'img': 'faculty/aishwarya.png'
    },

}


def load():
    for key, data in faculty_data.items():
        FacultyMember.objects.get_or_create(**data)
    print("Data added/updated successfully!")
