global mgh_version Linux-centos6_x86_64-stable-pub

Name: freesurfer
Version: 5.3.0
Release: 1%{?dist}
Summary: A suite for processing and analyzing (human) brain MRI images.
License: https://surfer.nmr.mgh.harvard.edu/fswiki/FreeSurferSoftwareLicense
URL: https://surfer.nmr.mgh.harvard.edu/
Source0: %{name}-%{mgh_version}-v%{version}.tar.gz-partaa
Source1: %{name}-%{mgh_version}-v%{version}.tar.gz-partab
Source2: %{name}-%{mgh_version}-v%{version}.tar.gz-partac
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Autoprov: 0
Autoreq: 0

%description
An open source software suite for processing and analyzing (human) brain MRI images.
 * Skullstripping
 * Image Registration
 * Subcortical Segmentation
 * Cortical Surface Reconstruction
 * Cortical Segmentation
 * Cortical Thickness Estimation
 * Longitudinal Processing
 * fMRI Analysis
 * Tractography
 * FreeView Visualization GUI
 * and much more ...

%prep

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{buildroot}/opt
cd %{buildroot}/opt
cat %{S:0} %{S:1} %{S:2} | tar xz
mv %{name} %{name}-%{version}
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
cat <<EOF > %{buildroot}%{_sysconfdir}/profile.d/%{name}.sh
# set paths for freesurfer
export FREESURFER_HOME=/opt/%{name}-%{version}
source \${FREESURFER_HOME}/SetUpFreeSurfer.sh
EOF
cat <<EOF >  %{buildroot}%{_sysconfdir}/profile.d/%{name}.csh
# set paths for freesurfer
setenv FREESURFER_HOME /opt/%{name}-%{version}
source \${FREESURFER_HOME}/SetUpFreeSurfer.csh
EOF

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/opt/%{name}-%{version}
%{_sysconfdir}/profile.d/%{name}.csh
%{_sysconfdir}/profile.d/%{name}.sh

%changelog
* Tue Nov 3 2015 Adrian Alves <alvesadrian@fedoraproject.org> - 5.3.0-1
- Initial build.
