document.addEventListener('DOMContentLoaded', () => {
  // Navigation handling
  const navItems = document.querySelectorAll('.nav-item');
  const sections = document.querySelectorAll('.section');

  navItems.forEach(item => {
      item.addEventListener('click', () => {
          navItems.forEach(nav => nav.classList.remove('active'));
          item.classList.add('active');

          const sectionId = item.dataset.section;
          sections.forEach(section => {
              section.classList.remove('active');
              if (section.id === sectionId) {
                  section.classList.add('active');
              }
          });
      });
  });

  // EC2 Instance Management
  const createInstanceForm = document.querySelector('.create-instance-form');
  if (createInstanceForm) {
      createInstanceForm.addEventListener('submit', (e) => {
          e.preventDefault();

          const instanceName = document.getElementById('instance-name').value;
          const instanceType = document.getElementById('instance-type').value;
          const amiType = document.getElementById('ami-type').value;
          const keyPair = document.getElementById('key-pair').value;

          fetch("http://localhost:8000/api/ec2/create", {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify({
                  instance_name: instanceName,
                  instance_type: instanceType,
                  ami: amiType,
              })
          })
          .then(response => response.json())
          .then(data => {
              alert("EC2 instance created successfully!");
              createInstanceForm.reset();
          })
          .catch(error => console.error("Error:", error));
      });
  }

  // S3 Bucket Management
  const createBucketForm = document.querySelector('.create-bucket-form');
  if (createBucketForm) {
      createBucketForm.addEventListener('submit', (e) => {
          e.preventDefault();

          const bucketName = document.getElementById('bucket-name').value;
          const region = document.getElementById('bucket-region').value;

          fetch("http://localhost:8000/api/s3/create", {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify({
                  bucket_name: bucketName,
                  region: region
              })
          })
          .then(response => response.json())
          .then(data => {
              alert("Bucket created successfully!");
              createBucketForm.reset();
          })
          .catch(error => console.error("Error:", error));
      });
  }

  const deleteBucketForm = document.querySelector('.delete-bucket-form');
  if (deleteBucketForm) {
      deleteBucketForm.addEventListener('submit', (e) => {
          e.preventDefault();

          const bucketName = document.getElementById('delete-bucket').value;

          if (confirm(`Are you sure you want to delete bucket "${bucketName}"?`)) {
              fetch(`http://localhost:8000/api/s3/delete/${encodeURIComponent(bucketName)}`, {
                  method: "DELETE"
              })
              .then(response => response.json())
              .then(data => {
                  alert("Bucket deleted successfully!");
                  deleteBucketForm.reset();
              })
              .catch(error => console.error("Error:", error));
          }
      });
  }

  // Route53 DNS Management
  const createZoneForm = document.querySelector('.create-zone-form');
  if (createZoneForm) {
      createZoneForm.addEventListener('submit', (e) => {
          e.preventDefault();

          const zoneName = document.getElementById('zone-name').value;

          fetch("http://localhost:8000/api/route53/zone/create", {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify({ zone_name: zoneName })
          })
          .then(response => response.json())
          .then(data => {
              alert("DNS zone created successfully!");
              createZoneForm.reset();
          })
          .catch(error => console.error("Error:", error));
      });
  }

  const manageDNSForm = document.querySelector('.manage-dns-form');
  if (manageDNSForm) {
      manageDNSForm.addEventListener('submit', (e) => {
          e.preventDefault();

          const zoneId = document.getElementById('zone-id').value;
          const recordName = document.getElementById('record-name').value;
          const recordType = document.getElementById('record-type').value;
          const recordValue = document.getElementById('record-value').value;

          fetch("http://localhost:8000/api/route53/record/create", {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify({
                  zone_id: zoneId,
                  record_name: recordName,
                  record_type: recordType,
                  record_value: recordValue
              })
          })
          .then(response => response.json())
          .then(data => {
              alert("DNS record created successfully!");
              manageDNSForm.reset();
          })
          .catch(error => console.error("Error:", error));
      });
  }

  const deleteZoneForm = document.querySelector('.delete-zone-form');
  if (deleteZoneForm) {
      deleteZoneForm.addEventListener('submit', (e) => {
          e.preventDefault();

          const zoneId = document.getElementById('delete-zone-id').value;

          if (confirm(`Are you sure you want to delete zone "${zoneId}"?`)) {
              fetch(`http://localhost:8000/api/route53/zone/delete?zone_id=${encodeURIComponent(zoneId)}`, {
                  method: "DELETE"
              })
              .then(response => response.json())
              .then(data => {
                  alert("DNS zone deleted successfully!");
                  deleteZoneForm.reset();
              })
              .catch(error => console.error("Error:", error));
          }
      });
  }

  // Refresh buttons
  const refreshButtons = {
      'refresh-instances': 'Refreshing instances...',
      'refresh-buckets': 'Refreshing buckets...',
      'refresh-zones': 'Refreshing zones...'
  };

  Object.entries(refreshButtons).forEach(([id, message]) => {
      const button = document.getElementById(id);
      if (button) {
          button.addEventListener('click', () => {
              button.classList.add('loading');
              console.log(message);
              setTimeout(() => {
                  button.classList.remove('loading');
              }, 1000);
          });
      }
  });
});
